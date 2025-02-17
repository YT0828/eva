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

from src.catalog.catalog_manager import CatalogManager
from src.planner.rename_plan import RenamePlan
from src.executor.abstract_executor import AbstractExecutor


class RenameExecutor(AbstractExecutor):

    def __init__(self, node: RenamePlan):
        super().__init__(node)

    def validate(self):
        pass

    def exec(self):
        """rename table executor

        Calls the catalog to modified metadata corresponding to the table.
        """

        new_table_name = self.node.new_name.table_name
        table_id = self.node.table_id
        CatalogManager().rename_table(new_table_name, table_id)
