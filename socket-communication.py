import socket
import sys
import time

remote_ip = "192.168.0.188" # The local address of my Siglent SDS 1202X-E
port = 5025 # Socket port provided by the oscilloscope
count = 0

def SocketConnect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Connecting to socket")
        s.connect((remote_ip, port))
        s.settimeout(5) # Don't hang on failure
        print(f"Connected: {s.getsockname()}")
    except socket.error as e:
        print(f"Failed to connect to {remote_ip}: {e}")
        s.close()
        sys.exit();
    return s

def SocketQuery(Sock, cmd):
    Sock.sendall(cmd)
    reply = b''
    while not reply.endswith(b'\n'):
        chunk = Sock.recv(4096)
        if not chunk:
            raise ConnectionError('Scope closed the connection')
        reply += chunk
    return reply.strip()

def SocketClose(Sock):
    Sock.close()
    time.sleep(.300)

def main():
    global remote_ip
    global port
    global count

    s = SocketConnect()

    # Send the *IDN? command 10 times
    # and print the response
    for i in range(10):
        qStr = SocketQuery(s, b'*IDN?\n')
        print(str(count) + ":: " + str(qStr))
        count = count + 1

    # Get the Channel 1 vertical scale
    print(SocketQuery(s, b'C1:VDIV?\n'))

    # Get all data from Channel 1
    print(SocketQuery(s, b'C1:PAVA? ALL\n'))

    SocketClose(s)
    input('Press "Enter" to exit')

if __name__ == '__main__':
    proc = main()
