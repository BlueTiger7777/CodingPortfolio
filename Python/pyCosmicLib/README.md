# pyCosmicLib Documentation
This modual contains various functions and classes

## Contents
- [Classes](#classes)
- [Functions](#functions)

## Classes

| Class Name               | Returns      | Description                                                  |
| ---                      | ---          | ---                                                          |
| [`tcolour`](#tcolour)    | `string`     | Returns a string escape code for the desired colour          |
| [`anchor`](#anchor)      | `[int, int]` | Returns a cordinate pair for fixed positions in the terminal |

### tcolour
`tcolour.{format}` returns `string`
This class contains the escape codes to format printed text in the terminal

| Format       | Escape Code  | Colour                                    |
| ---          | ---          | ---                                       |
| `ENDC`       | `'\33[0m'`   | Ends formatting                           |
| `BOLD`       | `'\33[1m'`   | Bold text                                 |
| `GREY`       | `'\33[2m'`   | Grey text                                 |
| `ITALLIC`    | `'\33[3m'`   | Itallic text                              |
| `UNDERLINE`  | `'\33[4m'`   | Underlined text                           |
| `BLINK`      | `'\33[5m'`   | Blinking text                             |
| `BLINK2`     | `'\33[6m'`   | Blinking text                             |
| `SELECTED`   | `'\33[7m'`   | Selected/Highlighted text                 |
| `TERM`       | `'\33[8m'`   | Text with the same colour as the terminal |
| `STRIKE`     | `'\33[9m'`   | Strike through text                       |
| `UNDERLINE2` | `'\33[21m'`  | Double underlined text                    |
| `BLACK`      | `'\33[30m'`  | Black text                                |
| `RED`        | `'\33[31m'`  | Red text                                  |
| `GREEN`      | `'\33[32m'`  | Green text                                |
| `YELLOW`     | `'\33[33m'`  | Yellow text                               |
| `BLUE`       | `'\33[34m'`  | Blue text                                 |
| `PURPLE`     | `'\33[35m'`  | Purple text                               |
| `CYAN`       | `'\33[36m'`  | Cyan text                                 |
| `WHITE`      | `'\33[37m'`  | White text                                |
| `BLACKBG`    | `'\33[40m'`  | Black background                          |
| `REDBG`      | `'\33[41m'`  | Red background                            |
| `GREENBG`    | `'\33[42m'`  | Green background                          |
| `YELLOWBG`   | `'\33[43m'`  | Yellow background                         |
| `BLUEBG`     | `'\33[44m'`  | Blue background                           |
| `PURPLEBG`   | `'\33[45m'`  | Purple background                         |
| `CYANBG`     | `'\33[46m'`  | Cyan background                           |
| `WHITEBG`    | `'\33[47m'`  | White background                          |
| `BBLACK`     | `'\33[90m'`  | Bright black text                         |
| `BRED`       | `'\33[91m'`  | Bright red text                           |
| `BGREEN`     | `'\33[92m'`  | Bright green text                         |
| `BYELLOW`    | `'\33[93m'`  | Bright yellow text                        |
| `BBLUE`      | `'\33[94m'`  | Bright blue text                          |
| `BPURPLE`    | `'\33[95m'`  | Bright purple text                        |
| `BCYAN`      | `'\33[96m'`  | Bright cyan text                          |
| `BWHITE`     | `'\33[97m'`  | Bright white text                         |
| `BBLACKBG`   | `'\33[100m'` | Bright black background                   |
| `BREDBG`     | `'\33[101m'` | Bright red background                     |
| `BGREENBG`   | `'\33[102m'` | Bright green background                   |
| `BYELLOWBG`  | `'\33[103m'` | Bright yellow background                  |
| `BBLUEBG`    | `'\33[104m'` | Bright blue background                    |
| `BPURPLEBG`  | `'\33[105m'` | Bright purple background                  |
| `BCYANBG`    | `'\33[106m'` | Bright cyan background                    |
| `BWHITEBG`   | `'\33[107m'` | Bright white background                   |

Example Code:
```py
from pyCosmicLib import tcolour as c
print(f'{c.BLINK}{c.RED}Example String{c.ENDC}')
```
> [!NOTE]
> The format name of the escape codes are bassed off of the Windows 11 PowerShell

### anchor
`anchor.{pos}` returns `[int, int]`
> [!NOTE]
> The anchor class only works when the script is ran in a terminal
## Functions
