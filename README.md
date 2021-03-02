# Game of Jacks

Simple card game

## Pre-requisites

1. [Python](https://www.python.org/)

   Have Python installed in your local development machine

2. [Pipenv](https://pypi.org/project/pipenv/)
   
   Have pipenv installed to install dependencies 

## Getting started

This will get you started with the project.

### Step 1

Install the dependencies required with pipenv

```bash
export PIPENV_VENV_IN_PROJECT=true
pipenv install
```

> This will also set your virtualenv
 
### Step 2

Run the cli program once you have the virtualenv setup, typically this can
be done with the command source

```bash
source <YOUR_WORKING_DIR>>/<PROJECT_DIR>/.venv/bin/activate
python cli.py <URL_PATH_TO_JSON>
```

> Where <URL_PATH_TO_JSON> is a link to the JSON file

Expected result should be something like below:

```plain
  Hand    Player A Score    Player B Score  Winner
------  ----------------  ----------------  -------------------------
     1                18                18  Player B
                                             (Q is higher than J)
     2                20                24  Player A
     3                23                20  Player B
     4                20                30  Player A
     5                19                30  Player A
     6                13                24  Player A
     7                13                30  Player A
     8                12                14  Player B
     9                24                20  Player B
    10                23                16  Player B
    11                26                13  Player B
    12                24                20  Player B
    13                12                24  Player A
    14                12                27  Player A
    15                30                 7  Player B
    16                22                20  Player B
    17                20                15  Player A
    18                30                13  Player B
    19                15                20  Player B
    20                17                22  Player A
    21                14                13  Player A
    22                23                14  Player B
    23                24                15  Player B
    24                15                30  Player A
    25                30                20  Player B
    26                24                20  Player B
    27                25                14  Player B
    28                24                20  Player B
    29                22                14  Player B
    30                22                20  Player B
    31                27                12  Player B
    32                20                30  Player A
    33                15                30  Player A
    34                23                16  Player B
    35                20                13  Player A
    36                20                22  Player A
    37                20                20  Player B
                                             (8H is higher than 8C)
    38                30                13  Player B
    39                22                13  Player B
    40                23                14  Player B
    41                26                20  Player B
    42                17                22  Player A
    43                30                12  Player B
    44                23                12  Player B
    45                30                13  Player B
    46                 5                14  Player B
    47                23                14  Player B
    48                17                30  Player A
    49                12                27  Player A
    50                24                13  Player B
    51                30                16  Player B
    52                23                20  Player B
    53                12                13  Player B
    54                30                 5  Player B
    55                 6                20  Player B
    56                22                20  Player B
    57                27                12  Player B
    58                14                20  Player B
    59                13                20  Player B
    60                20                15  Player A
    61                24                20  Player B
    62                23                16  Player B
    63                12                27  Player A
    64                20                20  Player A
                                             (J is higher than 10)
    65                20                22  Player A
    66                22                20  Player B
    67                24                15  Player B
    68                20                19  Player A
    69                30                19  Player B
    70                20                22  Player A
    71                23                12  Player B
    72                22                14  Player B
    73                24                20  Player B
    74                30                 9  Player B
    75                24                12  Player B
    76                30                16  Player B
    77                20                14  Player A
    78                20                25  Player A
    79                23                20  Player B
    80                21                21  Player A
                                             (A is higher than 9)
    81                24                20  Player B
    82                19                30  Player A
    83                14                12  Player A
    84                24                15  Player B
    85                27                20  Player B
    86                17                22  Player A
    87                14                23  Player A
    88                16                30  Player A
    89                24                12  Player B
    90                30                20  Player B
    91                21                21  Player A
                                             (AS is higher than AC)
    92                30                20  Player B
    93                18                18  Player B
                                             (9C is higher than 9D)
    94                30                14  Player B
    95                19                30  Player A
    96                24                15  Player B
    97                30                16  Player B
    98                23                20  Player B
    99                14                30  Player A
   100                22                20  Player B
   101                15                24  Player A
   102                22                 7  Player B
   103                20                24  Player A
   104                20                13  Player A
   105                30                19  Player B
   106                18                18  Player A
                                             (10S is higher than 10H)
   107                18                17  Player A
   108                15                15  Player A
                                             (6 is higher than 10)
   109                20                20  Player A
                                             (8H is higher than 8C)
   110                28                22  Player B

```

