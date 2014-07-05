# !/usr/bin/env python

##############################################################################
##  DendroPy Phylogenetic Computing Library.
##
##  Copyright 2010 Jeet Sukumaran and Mark T. Holder.
##  All rights reserved.
##
##  See "LICENSE.txt" for terms and conditions of usage.
##
##  If you use this work or any portion thereof in published work,
##  please cite it as:
##
##     Sukumaran, J. and M. T. Holder. 2010. DendroPy: a Python library
##     for phylogenetic computing. Bioinformatics 26: 1569-1571.
##
##############################################################################

"""
Tests for general NEXML tree list reading.
"""

import sys
import unittest
import dendropy
from dendropy.test.support import dendropytest
from dendropy.test.support import standard_file_test_trees
from dendropy.test.support import curated_test_tree
from dendropy.test.support import pathmap
if not (sys.version_info.major >= 3 and sys.version_info.minor >= 4):
    from dendropy.utility.filesys import pre_py34_open as open

class NexmlStandardTreeListReaderTestCase(
        standard_file_test_trees.StandardTreeListReaderTestCase,
        dendropytest.ExtendedTestCase):

    @classmethod
    def setUpClass(cls):
        standard_file_test_trees.StandardTreeListReaderTestCase.create_class_data(
                cls,
                schema="nexml",
                distinct_nodes_and_edges=True,
                distinct_taxa_and_labels_on_tree=True,
                taxa_on_tree_equal_taxa_in_taxon_namespace=False,
                )

    ## NOTE: many tests are in standard_file_test_trees.StandardTreeListReaderTestCase !! ##

    def test_collection_comments_and_annotations(self):
        tree_file_title = 'standard-test-trees-n33-annotated'
        tree_reference = standard_file_test_trees.tree_references[tree_file_title]
        expected_non_metadata_comments = tree_reference["tree_list_comments"]
        expected_metadata_comments = tree_reference["tree_list_metadata_comments"]
        expected_metadata = tree_reference["tree_list_metadata"]
        tree_filepath = self.schema_tree_filepaths[tree_file_title]
        tree_list = dendropy.TreeList.get_from_path(
                tree_filepath,
                "nexml")
        expected_comments = expected_non_metadata_comments
        self.compare_annotations_to_json_metadata_dict(
                tree_list,
                expected_metadata,
                coerce_metadata_values_to_string=True)
        self.assertEqual(len(tree_list.comments), len(expected_comments))
        self.assertEqual(set(tree_list.comments), set(expected_comments))
        self.verify_standard_trees(
                tree_list=tree_list,
                tree_file_title=tree_file_title,
                tree_offset=0,
                suppress_internal_node_taxa=True,
                suppress_leaf_node_taxa=False,
                metadata_extracted=extract_comment_metadata,
                coerce_metadata_values_to_string=True,
                distinct_nodes_and_edges=False,
                taxa_on_tree_equal_taxa_in_taxon_namespace=True)

if __name__ == "__main__":
    unittest.main()