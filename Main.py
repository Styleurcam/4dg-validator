import re
import sys


def main() -> None:
    with open(sys.argv[1]) as arg:
        file: str = arg.read()
        print(file)

    validate_4d = re.compile(pattern=r'''
    ^(?!(?:^#.*?(?:\n|$))*(?:(?:^(?:(?:Adapter|Straight(?:Bare)?)([2468])To(?!\1)[2468]|Bank(?:Down|Up)(?:Bare)?[2468]|B
    end(?:Wide)?(?:Bare|WallIn|WallOut)?[2468]|Cliff(?:Down|Up)[2468]|EndContinue(?:Bare)?2(?:To4)?|EndContinue(?:Bare)?
    4(?:To[26])?|EndContinue(?:Bare)?([68])(?:To(?!\2)[2468])?|(?:F|K|T|X|Y|Loop|Micro|Open|Slope(?:Up|Down)|StartEdge|E
    ndEdge|Straight)(?:Bare)?[2468]|Hill(?:Micro|Small)?(?:Down|Up)(?:Bare)?[2468]|Ramp(?:Down|Up)?(?:Bare)?[2468]|Skew(
    ?:Slope(?:Down|Up))?(?:Bare)?[2468]|Slot(?:Offset)?[468]|Start(?:Bare)?8(?:To6)?|Start(?:Bare)?6(?:To[48])?|Start(?:
    Bare)?([24])(?:To(?!\3)[2468])?|Turn(?:Skew)?(?:(?<=Skew)Short|Bare)?[2468]|Cone(?:4|s[68]|Wall[24])|(?:(?:Cub|Spher
    |Duocyl)inder|DoubleRotator|Elevator|Igloo|Platform|PopBumper|Shim|Spinner(?:Side|sIn|sOut|Large)|SpringBoard|Tetra|
    Trirect|Wedge|Cube)4|(?:Glome|Horn|SpinDisk|Well)6|Pyramid8|Windmill2|Null|)(?:,[0-3])?(?:\.|!|!\.|\.!)?[@^$*~]?|<([
    0-4]),(?!\4)[0-4],\d+?(?:\.\d+?)?>|<\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?>)(?:\n|$)))(?:.*
    ?(?:\n|$))'''.replace('\n    ', ''), flags=re.M)

    validate_5d = re.compile(pattern=r'''^(?!(?:#.*?(?:\n|$))*(?:^(?:(?:(?:Adapter|Straight(?:Bare)?)([2468])To(?!\1)[24
    68]|Bend(?:Wide)?(?:Bare)?[2468]|EndContinue(?:Bare)?2(?:To4)?|EndContinue(?:Bare)?4(?:To[26])?|EndContinue(?:Bare)?
    ([68])(?:To(?!\2)[2468])?|(?:F|T|Turn|XX?|YL?|Loop|Micro|Open|EndEdge|Straight|StartEdge)(?:Bare)?[2468]|Hill(?:Smal
    l)?(?:Down|Up)(?:Bare)?[2468]|HillMicro(?:Down|Up)[2468]|Ramp(?:Down|Up)[2468]|(?:SkewSlope(?:Down|Up)|Skew|Slope(?:
    Down|Up))[2468]|Start(?:Bare)?8(?:To6)?|Start(?:Bare)?6(?:To[48])?|Start(?:Bare)?([24])(?:To(?!\3)[2468])?|(?:(?:Bla
    ck|White)(?:Knight|Pawn)|WhiteKing|Cube|Eye|Platform|SpinnerLarge[AB]|Duocylinder|SpringBoard|(?:Tetra|Tri)rect)4|Sp
    inDisk6|Null|)(?:,(?:1?[0-9]|2[0-3]))?(?:\.|!|!\.|\.!)?[@^$*~]?|<([0-4]),(?!\4)[0-4],\d+?(?:\.\d+?)?>|<\d+?(?:\.\d+?
    )?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?>)(?:\n|$))).*?(?:\n|$)
    '''.replace('\n    ', ''), flags=re.M)

    valid_themes = [
        "#Theme Forest4D",
        "#Theme Sand4D",
        "#Theme Snow4D",
        "#Theme Abstract4D",
        "#Theme Lava4D",
        "#Theme Space4D",
        "#Theme Empty4D",
        "#Theme Finale5D",
        "#Theme Challenge5D"
    ]

    themes_5d = [
        "#Theme Finale5D",
        "#Theme Challenge5D"
    ]

    themes_4d = [
        "#Theme Forest4D",
        "#Theme Sand4D",
        "#Theme Snow4D",
        "#Theme Abstract4D",
        "#Theme Lava4D",
        "#Theme Space4D",
        "#Theme Empty4D"
    ]

    lines = file.split('\n')

    selected_lines = [line for line in lines if line in valid_themes]
    final_theme = selected_lines[-1] if selected_lines else None

    if not re.match(r'^#Name(.|\s)*?$', file, flags=re.M):
        print("no name defined")

    newline = '\n'
    if final_theme in themes_5d:
        if not re.findall(
                r'^#Ball \d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?\s*?$',
                file, flags=re.M) and "." not in file:
            print("invalid Ball parameters")

        if not re.findall(
                r'^#Hole \d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)? \d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?\s*?$',
                file, flags=re.M) and "!" not in file:
            print("invalid Hole parameters")

        if n := re.search(validate_5d, file):
            print(n)
            print(f"this is an invalid 5D 4dg level file, first error at line {file[:file.find(n.group(0))].count(newline) + 1}:\n{n[0][:-1]}")
        else:
            print(n)
            print("this is a valid 5D 4dg level file")

    elif final_theme in themes_4d:
        if not re.findall(r'^#Ball \d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?\s*?$', file,
                          flags=re.M) and "." not in file:
            print("invalid Ball parameters")

        if not re.findall(
                r'^#Hole \d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)? \d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?,\d+?(?:\.\d+?)?\s*?$',
                file, flags=re.M) and "!" not in file:
            print("invalid Hole parameters")

        if n := re.search(validate_4d, file):
            print(n)
            print(f"this is an invalid 4D 4dg level file: line {file[:file.find(n.group(0))].count(newline) + 1}\n\"{n[0][:-1]}\"")
        else:
            print(n)
            print("this is a valid 4D 4dg level file")

    else:
        print("no theme defined")


if __name__ == "__main__":
    main()
