
def comparing_versions(version_one, version_two):
    version_one_split = version_one.split(".")
    version_two_split = version_two.split(".")

    if version_one_split == version_two_split:
        return f'Version {version_one} is equals {version_two}'

    for i, subversion in enumerate(version_one_split):
        if i >= len(version_two_split):
            return f'Version {version_one} is bigger than {version_two}'

        if subversion > version_two_split[i]:
            return f'Version {version_one} is bigger than {version_two}'

    return f'Version {version_one} is smaller than {version_two}'

