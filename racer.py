import random

slots = []
## Each smolRacer has a score, defaults to 100 but can be boosted up to 150
smolRacers = [
    { "id": 0, "score": 100 },
    { "id": 1, "score": 125 },
    { "id": 2, "score": 150 },
    { "id": 3, "score": 100 },
    { "id": 4, "score": 100 },
    { "id": 5, "score": 150 },
    { "id": 6, "score": 100 },
    { "id": 7, "score": 125 },
    { "id": 8, "score": 100 },
    { "id": 9, "score": 150 },
    { "id": 11, "score": 100 },
    { "id": 12, "score": 100 },
    { "id": 13, "score": 125 },
    { "id": 14, "score": 100 },
    { "id": 15, "score": 150 },
    { "id": 16, "score": 100 },
    { "id": 17, "score": 100 },
    { "id": 18, "score": 150 },
    { "id": 19, "score": 100 },
    { "id": 20, "score": 125 },
]

print("initializing slots...")
lastInterval = 0
# as each smolRacer stakes their smol into the racing contract we create a new slot for them
for smolRacer in smolRacers:

    id = smolRacer['id']
    score = smolRacer['score']
    nextInterval = lastInterval + score

    # assign smol a slot, e.g: [0, 100], [100, 225], [225, 375]
    smolSlot = {
        "id": smolRacer['id'],
        "start": lastInterval,
        "end": nextInterval
    }
    slots.append(smolSlot)
    lastInterval = nextInterval
    print("smolSlot_{}: ".format(smolRacer['id']), smolSlot)



def drawWinner():
    winningDraw = random.randint(1, lastInterval)
    winningSlots = []
    for i, slot in enumerate(slots):
        if isInSlot(winningDraw, slot):
            printWinningSlot(winningDraw, slot)
            winningSlots.append(slot)
            break

    print("winning slots: {}".format(winningSlots))




def draw3Winners():
    winningDraws = [
        random.randint(1, lastInterval),
        random.randint(1, lastInterval),
        random.randint(1, lastInterval),
    ]
    winningSlots = []

    for winningDraw in winningDraws:
        for i, slot in enumerate(slots):
            if isInSlot(winningDraw, slot):
                printWinningSlot(winningDraw, slot)
                alreadySampled = isSlotAlreadySampled(slot, winningSlots)
                print("alreadySampled {}".format(alreadySampled))
                winningSlots.append(slot)
                break

    print("winning slots: {}".format(winningSlots))



## Helper functions

def isInSlot(winningDraw, slot):
    return slot["start"] < winningDraw and winningDraw <= slot["end"]

def isSlotAlreadySampled(slot, winningSlots):
    isAlreadySampled = False
    for s in winningSlots:
        if slot["id"] == s["id"]:
            isAlreadySampled = True
    return isAlreadySampled

def printWinningSlot(winningDraw, slot):
    print("winningDraw {a} lies in [{b}, {c}] of slot {d}".format(
        a=winningDraw,
        b=slot["start"],
        c=slot["end"],
        d=slot["id"],
    ))
    print("smol {} won!".format(slot["id"]))



print("\n\n===== Draw 1 winner")
drawWinner()

print("\n\n===== Draw 3 winners")
draw3Winners()