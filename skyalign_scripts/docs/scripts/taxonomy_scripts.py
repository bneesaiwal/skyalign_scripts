#!/usr/bin/python Python

"""
This script takes previously creates taxonomy files and represents them in trees

@Author Aneel Biswas
@Version 0.1
@Date 2022Aug19
"""

from __future__ import annotations
from TaxonomyTree import TaxonomyTree, TaxonomyNode


euk_prot_csv = '/Users/aneelbiswas/Documents/JoulineLabWork/EukProt_included_data_sets.v02.2020_06_30(1).txt'
pro_taxonomy = '/Users/aneelbiswas/Documents/JoulineLabWork/CompleteTaxonomyData/corrected_taxonomy2.txt'


def get_pro_taxonomy(taxon_file: str = pro_taxonomy) -> TaxonomyTree:
    pro_tree = TaxonomyTree()
    with open(taxon_file, 'r', encoding='utf8') as taxons:
        for line in taxons:
            genome_id, tax_info = line.split('\t')
            parent = ''
            for clade in tax_info.split(';'):
                pro_tree.add_node(clade, parent)
                parent = clade
    print(pro_tree)
    return pro_tree


def main() -> None:
    get_pro_taxonomy()
    return None


if __name__ == "__main__":
    main()
