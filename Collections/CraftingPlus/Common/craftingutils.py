# Define some constants
kpl_cc = "Knowledge from a Past Life"
fog_cc = "Flash of Genius"

# Define some functions
def extract_roll_bonuses(args, ch):
    """
    Extracts the roll bonuses from the given arguments and character object.

    Args:
        args: The arguments passed to the function.
        ch: The character object.

    Returns:
        A list of roll bonuses.
    """
    rollString = ""
    extraFields = ""
    # Collect manual roll bonuses to a string
    bonus = args.join("b", "+")

    # Check for guidance
    guidance = "+1d4[guidance]" if args.last("guidance") else ""

    # Collect manual roll bonuses to the rollString variable
    if bonus:
        rollString += f"+{bonus}"

    # Add guidance if it was specified
    if guidance != "":
        rollString += guidance
        extraFields += f"""-f "Guidance|Once before the spell ends, the target can roll a d4 and add the number rolled to one ability check of its choice. It can roll the die before or after making the ability check. The spell then ends." """
    
    # Add Knowledge from a Past Life and update Counter
    if args.last("kpl") and ch.cc_exists(kpl_cc) and ch.get_cc(kpl_cc) > 0:
        rollString += "+1d6[kpl]"
        ch.mod_cc(kpl_cc, -1)
        extraFields += f"""-f "{kpl_cc}|You temporarily remember glimpses of the past, perhaps faded memories from ages ago or a previous life. When you make an ability check that uses a skill, you can roll a d6 immediately after seeing the number on the d20 and add the number on the d6 to the check.\n{ch.cc_str(kpl_cc)}" """
    elif args.last("kpl") and ch.cc_exists(kpl_cc) and ch.get_cc(kpl_cc) == 0:
        extraFields += f"""-f "{kpl_cc}|You must take a long rest to regain your expended uses.\n{ch.cc_str(kpl_cc)}" """
    elif args.last("kpl") and not ch.cc_exists(kpl_cc):
        extraFields += f"""-f "{kpl_cc}|You do not have this ability." """

    # Add Flash of Genius and update Counter
    if args.last("fog") and ch.cc_exists(fog_cc) and ch.get_cc(fog_cc) > 0:
        rollString += f"+{ch.skills.intelligence.value}"
        ch.mod_cc(fog_cc, -1)
        extraFields += f"""-f "{fog_cc}|You gain the ability to come up with solutions under pressure. When you or another creature you can see within 30 feet of you makes an ability check or a saving throw, you can use your reaction to add your Intelligence modifier (**+{ch.skills.intelligence.value}**) to the roll.\n{ch.cc_str(fog_cc)}" """
    elif args.last("fog") and ch.cc_exists(fog_cc) and ch.get_cc(fog_cc) == 0:
        extraFields += f"""-f "{fog_cc}|You must take a long rest to regain your expended uses.\n{ch.cc_str(fog_cc)}" """
    elif args.last("fog") and not ch.cc_exists(fog_cc):
        extraFields += f"""-f "{fog_cc}|You do not have this ability." """
    
    # Finally, return the rollString and extraFields
    return (rollString, extraFields)

def pluralize_str(str):
    """
    Pluralizes the given string.

    Args:
        str: The string to pluralize.

    Returns:
        The pluralized string.
    """
    if str.endswith("s") or str.endswith("x") or str.endswith("z") or str.endswith("ch") or str.endswith("sh"):
        return f"{str}es"
    elif str.endswith("y") and str[-2] not in "aeiou":
        return f"{str[:-1]}ies"
    else:
        return f"{str}s"
