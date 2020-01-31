#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#if defined(__APPLE__)
#define COMMON_DIGEST_FOR_OPENSSL
#include <CommonCrypto/CommonDigest.h>
#define SHA1 CC_SHA1
#else
#include <openssl/md5.h>
#endif

char *str2md5(const char *str, int length) {
  int n;
  MD5_CTX c;
  unsigned char digest[16];
  char *out = (char*)malloc(33);
  MD5_Init(&c);
  while (length > 0) {
    if (length > 512) {
      MD5_Update(&c, str, 512);
    } else {
      MD5_Update(&c, str, length);
    }
    length -= 512;
    str += 512;
  }
  MD5_Final(digest, &c);
  for (n = 0; n < 16; ++n) {
    snprintf(&(out[n*2]), 16*2, "%02x", (unsigned int)digest[n]);
  }
  return out;
}


int main(int argc, char **argv) {
  int key[20], loop, x, i, o;
  time_t t = time(NULL);
  int year, mon, day, hour, min, sec, hour2, min2, sec2;
  char part[100];

  const char *inp_path = argv[1];
  FILE *fplaintext = fopen(inp_path, "r");

  fseek(fplaintext, 0L, SEEK_END);
  long size = ftell(fplaintext);
  rewind(fplaintext);


  char *plaintext = calloc(1, size+1);
  fread(plaintext, 1, size, fplaintext);
  fclose(fplaintext);
  struct tm tm = *localtime(&t);
  year = tm.tm_year + 1900;
  mon = tm.tm_mon +1;
  day = tm.tm_mday;
  hour= tm.tm_hour;
  min = tm.tm_min;
  sec = tm.tm_sec;
  hour2= tm.tm_hour;
  min2 = tm.tm_min;
  sec2 = tm.tm_sec;

  for (x= 3; x>-1; x--){
    key[x]=(year %10);
    year /= 10;
  }
  for (x= 5; x>3; x--){
    key[x]=(mon) %10;
    mon /= 10;
  }
  for (x= 7; x>5; x--){
    key[x]=(day) %10;
    day /= 10;
  }
  for (x= 9; x>7; x--){
    key[x]=(hour) %10;
    hour /= 10;
  }
  for (x= 11; x>9; x--){
    key[x]=(min) %10;
    min /= 10;
  }
  for (x= 13; x>11; x--){
    key[x]=(sec) %10;
    sec /= 10;
  }

  for (x= 15; x>13; x--){
    key[x]=(hour2) %10;
    hour2 /= 10;
  }
  for (x= 17; x>15; x--){
    key[x]=(min2) %10;
    min2/= 10;
  }
  for (x= 19; x>17; x--){
    key[x]=(sec2) %10;
    sec2/= 10;
  }


  for(i = 0; plaintext[i] != '\0'; ++i){
    if(plaintext[i] >= 'a' && plaintext[i] <= 'z'){
      plaintext[i] = plaintext[i] + key[i];
      if(plaintext[i] > 'z'){
        plaintext[i] = plaintext[i] - 'z' + 'a' - 1;
      }
      plaintext[i] = plaintext[i];
    }
    else if(plaintext[i] >= 'A' && plaintext[i] <= 'Z'){
      plaintext[i] = plaintext[i] + key[i];
      if(plaintext[i] > 'Z'){
        plaintext[i] = plaintext[i] - 'Z' + 'A' - 1;
      }
      plaintext[i] = plaintext[i];
    }
  }

  for(o=14; o<20; o++){
    part[o-14]=plaintext[o];
  }

  char *encrypt2 = str2md5(part, strlen(part));
  FILE *fencrypt2 = fopen("encrypt2.txt", "w");
  fwrite(encrypt2, 4, sizeof(encrypt2), fencrypt2);
  fclose(fencrypt2);
  printf("\nFind the secret message. Part of it is in Encrypt1.txt, encoded with base64. The rest of it has been hashed, Encrypt2.txt.\n");

  return 0;
}
