# SPDX-FileCopyrightText: 2022 Rot127 <unisono@quyllur.org>
# SPDX-License-Identifier: LGPL-3.0-only
from enum import StrEnum

from Transformer.Pures.Pure import Pure
from Transformer.Pures.PureExec import PureExec
from Transformer.helper import cast_operands


class CompareOpType(StrEnum):
    LT = "<"
    GT = ">"
    LE = "<="
    GE = ">="
    EQ = "=="
    NE = "!="


class CompareOp(PureExec):
    def __init__(self, name: str, a: Pure, b: Pure, op_type: CompareOpType):
        self.op_type = op_type
        a, b = cast_operands(a=a, b=b, immutable_a=False)

        PureExec.__init__(self, name, [a, b], a.value_type)

    def il_exec(self):
        sl = "S" if self.ops[0].value_type.signed else "U"
        if self.op_type == CompareOpType.LT:
            return f"{sl}LT({self.ops[0].il_read()}, {self.ops[1].il_read()})"
        elif self.op_type == CompareOpType.GT:
            return f"{sl}GT({self.ops[0].il_read()}, {self.ops[1].il_read()})"
        elif self.op_type == CompareOpType.LE:
            return f"{sl}LE({self.ops[0].il_read()}, {self.ops[1].il_read()})"
        if self.op_type == CompareOpType.GE:
            return f"{sl}GE({self.ops[0].il_read()}, {self.ops[1].il_read()})"
        elif self.op_type == CompareOpType.EQ:
            return f"EQ({self.ops[0].il_read()}, {self.ops[1].il_read()})"
        elif self.op_type == CompareOpType.NE:
            return f"INV(EQ({self.ops[0].il_read()}, {self.ops[1].il_read()}))"
        else:
            raise NotImplementedError(
                f"Compare operation {self.op_type} not implemented."
            )
