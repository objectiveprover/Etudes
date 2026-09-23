module Main (main) where

main :: IO ()
main = do
  fileContent <- file
  putStrLn fileContent

filePath :: FilePath
filePath = "./test.pdf"

file :: IO String
file = readFile filePath
