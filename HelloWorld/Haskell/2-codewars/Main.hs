module Main (main) where

main :: IO ()
main = do
  putStrLn (boolToWord True)
  putStrLn (boolToWord False)

boolToWord :: Bool -> String
boolToWord x = if x then "Yes" else "No"
