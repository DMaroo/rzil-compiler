# SPDX-FileCopyrightText: 2022 Rot127 <unisono@quyllur.org>
# SPDX-License-Identifier: LGPL-3.0-only

from math import ceil

from Transformer.Pures.LetVar import LetVar
from Transformer.Pures.Pure import ValueType, Pure


class Sizeof(LetVar):
    """sizeof operator according to ISO/IEC 9899:201x (C11 standard) - 6.5.3.4."""

    def __init__(self, name: str, op: Pure):
        self.name = name
        self.size = ceil(op.value_type.bit_width / 8)

        LetVar.__init__(self, name, self.size, ValueType(True, 32))
