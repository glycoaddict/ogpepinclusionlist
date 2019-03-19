"""
take a list of O-glycopeptides,
add on a database of O-glycans
give you the permutations for an inclusion list
output an excel/csv file for Orbitrap inclusion
"""

def initialise_salient_dict_keys():
    """
    df_index : human readable string
    :return:
    """
    desired_dict_keys_as_multiline_string = \
    """
    PARAMETER_VERSION    
    SpectraFiles
    DatabaseFiles
    add_decoys
    OutputFolder
    machine_type
    precursor_mass_error
    fragment_mass_error
    fragment_mass_error2
    lock_mass_list
    off_by_one
    protein_fdr_pulldown
    DigestLetters
    DigestCutterType
    DigestType
    maximum_missed_cleavages
    glycan_text
    common_max
    rare_max
    mod_text
    enable_promote_score_nglycan
    fragment_unit
    fragment_unit2
    """
    return parse_multiline_string(desired_dict_keys_as_multiline_string)


def parse_multiline_string(s):
    """
    this converts a multiline string into a list of individual lines=entries, stripped of white spaces
    and \n newlines.
    :param s:
    :return:
    """
    result = [x.strip() for x in s.strip().split('\n')]
    return result