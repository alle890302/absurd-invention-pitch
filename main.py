"""One-Sentence Absurd Invention Pitch — entry program.

Writes ONE sentence (<=220 chars) to /output/entry.txt: a pitch for a
ridiculous invention that fixes a tiny everyday annoyance.

Pass 1 draft: the rain-charged umbrella (annoyance: dead phone; bonus:
worse weather = more battery). Weighing it against the judge's ordered
criteria, the annoyance is a little generic and the laugh leans on the
ironic payoff line rather than the invention itself.

Pass 2 (final): the Forget-Me-Not Doorframe. The annoyance — walking
into a room and forgetting why — is smaller, more universal and more
recognisable; the laugh is intrinsic to the invention (a doorframe that
eavesdrops on your muttered errand and whispers it back as you cross);
and the mechanism is silly yet weirdly plausible in a smart-home world.
It also beats the other supplied candidates: the human snooze button's
annoyance (a talkative coworker) is less "tiny everyday", and the
excuse-playing doorbell's payoff is a quoted gag bolted onto the device.
"""

import os

PITCH = (
    "Meet the Forget-Me-Not Doorframe: it eavesdrops on you muttering "
    "'phone charger' in the kitchen and whispers it back as you cross "
    "the threshold, so you never again arrive in a room having "
    "forgotten why."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
