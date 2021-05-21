from kivy.clock import Clock
from kivy.properties import ListProperty, BoundedNumericProperty, DictProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy_garden.SimpleTableLayout import SimpleTableLayout
from kivy.garden import *

# garden_system_dir = "C:\\Users\\success\\.kivy\\garden"
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

print("app dir : ", garden_app_dir)
print("sys dir : ", garden_system_dir)
print("home dir : ", kivy_home_dir)


class DataTableLayout(SimpleTableLayout):

    # TODO : Right now if the table has both columns and rows headers, we must add columns' first before rows'.
    #  Have to handle this.

    table = ObjectProperty()
    data = ListProperty()
    col_headers = ListProperty()
    row_headers = ListProperty()

    # def __init__(self, cols, rows, **kwargs):
    #     super(DataTableLayout, self).__init__(**kwargs)
    #     self.cols = cols
    #     self.rows = rows
    #     self.data = [[TextInput(text=str(x)) for x in range(self.cols)] for y in range(self.rows)]
    #     Clock.schedule_once(self.show_table, 0)

    def __init__(self, *args, **kwargs):
        super(DataTableLayout, self).__init__(*args, **kwargs)
        self.cols = kwargs.get('cols', 10)
        self.rows = kwargs.get('rows', 5)
        self.data = [[TextInput(text=str(x)) for x in range(self.cols)] for y in range(self.rows)]
        Clock.schedule_once(self.show_table, 0)

    def on_col_headers(self, instance, value):
        # col_headers is a new row, the first row
        self.rows += 1
        col_titles = []
        for h in value:
            new_header = Button(text=h.value)
            col_titles.append(new_header)
        if self.row_headers:
            col_titles.insert(0, Button(text="Headers"))
        self.data.insert(0, col_titles)

    def on_row_headers(self, instance, value):
        # row_headers is a new column, the first one
        self.cols += 1
        row_titles = []
        for h in value:
            new_header = Button(text=h.value)
            row_titles.append(new_header)
        start, end, count, should_put_back_first_row = 0, self.rows, 0, False
        if self.col_headers:
            start = 1
            end = self.rows - 1
        for i in range(start, end):
            row = self.data[i]
            val = row_titles[count]
            row.insert(0, val)
            count += 1

    def set_cell_row_span(self, cell_x, cell_y, row_span):
        self.data[cell_y][cell_x].rowspan = row_span
        while row_span > 1:
            row_span = row_span - 1
            # when deleting cells in batch cells shift to the left, so if you want to delete a cell
            #  right under the current one you could have to look in lefter positions if the cell has already shifted
            while True:
                try:
                    c = self.data[cell_y + row_span][cell_x]
                    break
                except IndexError as e:
                    cell_x = cell_x - 1
            del self.data[cell_y + row_span][cell_x]

    def set_cell_col_span(self, cell_x, cell_y, col_span):
        self.data[cell_y][cell_x].colspan = col_span
        while col_span > 1:
            col_span = col_span - 1
            del self.data[cell_y][cell_x + col_span]

    def set_row_row_span(self, row_number, row_span):
        length = len(self.data[row_number])
        for col_pos in range(length):
            print("col_pos is : ", col_pos)
            self.set_cell_row_span(col_pos, row_number, row_span)

    def set_col_col_span(self, col_number, row_span):
        for row_pos in range(len(self.data)):
            print("row_pos is : ", row_pos)
            self.set_cell_col_span(col_number, row_pos, row_span)

    def set_cell_data(self, cell_x, cell_y, data):
        self.data[cell_y][cell_x].text = data

    def show_table(self, dt):
        for row in self.data:
            for cell in row:
                print("value is ", cell.text)
                if cell.text != 'header_strings':
                    self.add_widget(cell)


class MismatchRowsNumberException(Exception):
    pass


class MismatchColumsNumberException(Exception):
    pass


# from kivymd.app import MDApp


class Header:
    value = None
    row_span = 1
    col_span = 1

    def __init__(self, value):
        self.value = value


class TestApp(MDApp):

    def build(self):

        dt = DataTableLayout(cols=4, rows=6)
        dt.row_headers = [Header("student 1"), Header("student 2"), Header("student 3"),
                 Header("student 4"), Header("student 5"), Header("student 6"),]
        dt.col_headers = [Header("Maths"), Header("SVT"), Header("M"), Header("fgfg")]  # , "grte", "hgjjh"]
        # dt.set_cell_row_span(1, 2, 4)
        # dt.set_cell_col_span(1, 2, 2)
        # dt.set_row_row_span(1, 2)
        dt.set_col_col_span(2, 2)
        dt.set_cell_data(2, 2, "This should be none")
        return dt


if __name__ == "__main__":
    TestApp().run()
