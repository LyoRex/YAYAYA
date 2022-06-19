
# YAYAYA
### A Python interpreter of the YAYAYA coding language.

## USAGE
> python yayaya.py [filename]

## HOW THE LANGUAGE WORKS
YAYAYA is a language based around the phrase "yayaya". The entirety of YAYAYA source code is meant to be able to be read aloud but not necessarily discernable. THIS IS NOT A SERIOUS PROGRAMMING LANGUAGE because who in their right mind would be willing to write source code that looks like this:
> YAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAH
??YAH
YAYAH
YAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAH
YAYAH
YAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAH
AYAHAYAH
AYAYAH
!!YAH
YAYAH
YAYAYAHYAYAYAHYAYAYAH
YAYAYAYAH
YAYAH
YAYAYAHYAYAYAHYAYAYAHYAYAYAHYAYAYAH
YAYAYAYAH
AYAH
YAYAYAYAH

### Commands
| Command | Function |
| - | - |
| **YA** | Increment data pointer |
| **A** | Decrement data pointer|
| **YAYA** | Increment byte at the data pointer |
| **AYA** | Decrement byte at the data pointer |
| **YAYAYA** | Output the byte at the data pointer |
| **AYAYA** | Take one byte of input from stdin and store it at the data pointer |
| **??** | If the byte at the data pointer is 0, jump to the matching **!!** |
| **!!** | If the byte at the data pointer is not 0, jump back to the first command after the matching **??** |

Commands are delimited by **YAH**.
