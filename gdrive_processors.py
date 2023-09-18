import typing as t

import gspread

from constants import SERVICE_ACCOUNT, AVAILABLE_ROW_FOR_DICT


class GSheet:
    def __init__(self):
        self.spreadsheet_name = "khvostati_db"

    def _open_spreadsheet(self):
        google_creds = gspread.service_account_from_dict(SERVICE_ACCOUNT)
        return google_creds.open(self.spreadsheet_name)

    def _open_worksheet(self, worksheet_name: str):
        return self._open_spreadsheet().worksheet(worksheet_name)

    def get_all_data(
        self,
        worksheet_name: str
    ) -> list[dict[str, t.Any]]:
        '''Function to get all info from selected worksheet'''
        worksheet = self._open_worksheet(worksheet_name)
        return worksheet.get_all_records()

    def get_rows(
        self,
        worksheet_name: str,
        cells_scope: str
    ) -> list[list[str]]:
        '''Function to get an info from selected area. For example: 'A7:E9'''
        return self._open_worksheet(worksheet_name).get(cells_scope)

    def get_one_cell(
        self,
        worksheet_name: str,
        cell_name: str
    ) -> str:
        '''Function to get an info from only one cell. For example: 'A7'''
        return self._open_worksheet(worksheet_name).acell(cell_name)

    def update_row(
        self,
        worksheet_name: str,
        cells_scope: str,
        values: list[list[str]]
    ) -> list[list[str]]:
        '''Function to insert/update info to selected area. Example:'A7:E9'''
        return self._open_worksheet(worksheet_name).update(cells_scope, values)

    def next_available_row(
        self,
        worksheet_name: str
    ) -> str:
        row_count = sum(
            value is not None for value in self.get_all_data(worksheet_name)
        )
        return str(row_count + AVAILABLE_ROW_FOR_DICT)
