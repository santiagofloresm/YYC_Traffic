import tkinter as tk
import TableBuilder as Tb
import DatabaseQuery as Db


class RightFrame(tk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.build_frame()

    def build_frame(self, sort=None, collection=None, year=None):

        if sort is None or collection is None:
            # TODO clear screen before printing new table
            # I wrote this to do here but I can't figure out how or where to do this
            pass

        # If the collection is for Volume
        elif sort is not None and collection.startswith('TrafficFlow'):
            # If button sort clicked it will do this
            if sort == 'sorted':
                results = Db.Query().query(collection)
                tree = Tb.TableBuilder(results).build_table_flow("volume", year, 'sorted')
                tree.pack(fill='both', expand=True)
            # If button read clicked it will do this
            else:
                results = Db.Query().query(collection)
                tree = Tb.TableBuilder(results).build_table_flow("volume")
                tree.pack(fill='both', expand=True)

        # If collection is for Incidents
        elif sort is not None and collection.startswith('TrafficIncidents'):
            results = Db.Query().query(collection)
            # Because all the information comes from the same file here is where the data gets filtered for each year
            if year == '2016':
                # If button sort clicked it will go this
                if sort == 'sorted':
                    tree = Tb.TableBuilder(results).build_table_flow("incidents", '2016', 'sorted')
                    tree.pack(fill='both', expand=True)
                # If button read clicked it will do this
                else:
                    tree = Tb.TableBuilder(results).build_table_flow("incidents", '2016')
                    tree.pack(fill='both', expand=True)
            elif year == '2017':
                if sort == 'sorted':
                    tree = Tb.TableBuilder(results).build_table_flow("incidents", '2017', 'sorted')
                    tree.pack(fill='both', expand=True)
                else:
                    tree = Tb.TableBuilder(results).build_table_flow("incidents", '2017')
                    tree.pack(fill='both', expand=True)
            elif year == '2018':
                if sort == 'sorted':
                    tree = Tb.TableBuilder(results).build_table_flow("incidents", '2018', 'sorted')
                    tree.pack(fill='both', expand=True)
                else:
                    tree = Tb.TableBuilder(results).build_table_flow("incidents", '2018')
                    tree.pack(fill='both', expand=True)

