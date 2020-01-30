## For Solution 1
__1. First, you need to generate multiple frequency tables__
  * Find a couple of lengthy fairy tale stories
  * Generate their (fairy tales) respective frequency tables
  
__2. Next, create the ultimate frequency table (A)__
  * Combine the frequency tables generated into one big frequency table
  * __The final frequency table will be used to match with the frequncy table of the ciphertext__
 
__3. Similar to 1, generate a frequency table (B) for the ciphertext__
  * It is normal to get weird characters or alphabets as the highest frequency
  
__4. Do a 1-to-1 matching for the 2 frequency tables (A & B) *in order*__ 

__5. Upon matching, you will *NOT* get the original plaintext, but you do get something readable__
  * Make the neccesary changes to your matching algorithm (in this case, I did a bruteforce)
  * Keeping making changes until you get the full text
  * In my case, I went to search the original text after I deciphered to about 70% of the ciphertext
  
  
  ## For Solution 2
  Refer to __sol2.png__ for the formula used
