############### Stats #################
stats_params = {
# Read
"fragment_length" : 650,
"mapping_quality" : 20,
"base_quality" : 20,
# ALT
"dp_limit" : 5,
"alt_ratio_limit" : 0.2,
"sample_vote_limit" : 2,  
"vote_ratio_limit" : 0.9,
"snp_read_limit" : 1,
# Indel
"indel_ratio" : 0.05,
# Bulk
"bulk_ref_limit" : 1,  #this requires the remaining percent to be only a1 
"acceptable_bases" : ['A', 'C', 'G', 'T'],
}
############### Analyze #################
analyze_params = {
"dp_tuple_limit" : 5,
"snp_total_vote" : 0.9,
"snp_vote_ratio" : 0.9,

"tuples_ratio" : 0.9,
"tuples_internal_ratio" : 0.1,
"tuples_c2_external_error_ratio" : 0.1, # 1-tuples_ratio 

"c3_a1_limit" : 2,
"c3_homo_limit" : 2,

"homo_error_allowed" : 0,

"tuple_group_ratio" : 0.01,
"win_internal_group_ratio" : 0.1,

"sample_tuple_vote_limit" : 2,
"vote_tuple_ratio_limit" : 0.9,

"conflicting_upper_limit" : 0,
"c3_conflicting_upper_limit" : 0,
"a1_lower_limit" : 2,
"bulk_dp_interval" : (15,65), # Must have the following format (min, max)
}

################ Misc ##################
misc_params = {
"mut_nr_limit" : 1,
"mut_dist_limit" : 1000,

"snp_nr_limit" : 10,
"snp_dist_limit" : 1000,
}


trees = {
    'tree1':{
        'samples':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
        'params': { 'MIN_HET': 2, 'MIN_HOM': 1, 'MAX_HET': 14, 'MAX_HOM': 13}
    },
    'all':{
        'samples':['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'],
        'params': { 'MIN_HET': 2, 'MIN_HOM': 1, 'MAX_HET': 14, 'MAX_HOM': 13}
    }
}


