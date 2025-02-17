# coding=utf-8
# Copyright 2018-2020 EVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from src.parser.rename_statement import RenameTableStatement
from src.parser.table_ref import TableRef, TableInfo

from src.parser.evaql.evaql_parserVisitor import evaql_parserVisitor
from src.parser.evaql.evaql_parser import evaql_parser
import warnings


# Modified
##################################################################
# RENAME STATEMENTS
##################################################################
class RenameTable(evaql_parserVisitor):
    def visitOldtableName(self, ctx: evaql_parser.OldtableNameContext):

        table_name = self.visit(ctx.fullId())
        if table_name is not None:
            table_info = TableInfo(table_name=table_name)
            return table_info
        else:
            warnings.warn("Invalid from table", SyntaxWarning)
   
    def visitNewtableName(self, ctx: evaql_parser.NewtableNameContext):

        table_name = self.visit(ctx.fullId())
        if table_name is not None:
            table_info = TableInfo(table_name=table_name)
            return table_info
        else:
            warnings.warn("Invalid from table", SyntaxWarning)

    def visitRenameTable(self, ctx: evaql_parser.RenameTableContext):
        old_table_ref = TableRef(self.visit(ctx.oldtableName()))
        new_table_name = self.visit(ctx.newtableName())
        rename_stmt = RenameTableStatement(old_table_ref, new_table_name)
        return rename_stmt