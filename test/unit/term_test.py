#!/usr/bin/env python
# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2014, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

import unittest

from fluent.term import Term



class TermTest(unittest.TestCase):


  def test_subsample(self):
    term = Term().createFromBitmap([1, 3, 4, 6, 8, 9], width=3, height=3)
    self.assertEqual(term.sparsity, 100*2./3)
    term.subsample(34.0)
    self.assertEqual(len(term.bitmap), 3)
    self.assertEqual(term.sparsity, 100*1./3)


  def test_overSubsample(self):
    term = Term().createFromBitmap([1, 3, 4, 6, 8, 9], width=3, height=3)
    self.assertEqual(term.sparsity, 100*2./3)
    term.subsample(80.0)
    self.assertEqual(len(term.bitmap), 6)
    self.assertEqual(term.sparsity, 100*2./3)



if __name__ == '__main__':
  unittest.main()