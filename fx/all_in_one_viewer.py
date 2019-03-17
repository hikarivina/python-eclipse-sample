# ==============================================================================
# brief        All-in-One FX Viewerの描写
#
# author       たっきん
#
# 事前準備 :
#     oandapyV20のインストール (pip install oandapyV20)
#     Bokehのインストール（conda install bokeh）
# ==============================================================================
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox, gridplot
from bokeh.models.widgets import Select
from bokeh.io import curdoc

output_file("all-in-one_viewer.html")


class AllInOneViewer(object):

    def __init__(self):
        # Widgetセレクト（通貨ペア）
        widsel_ins = Select(title="通貨ペア:",
                            value="USD-JPY",
                            options=["USD-JPY", "EUR-JPY", "EUR-USD"])
        # Widgetセレクト（期間）
        widsel_gra = Select(title="期間:",
                            value="日足",
                            options=["週足", "日足", "４時間足", "１時間足",
                                     "３０分足", "１５分足", "１０分足",
                                     "５分足", "１分足"])

        self.__view = gridplot([[widsel_ins, widsel_gra],
                                [None, None],
                                [None, None]])

    def get_view(self):
        return self.__view


if __name__ == "__main__":
    """eclipse実行用"""
    viewer = AllInOneViewer()
    show(viewer.get_view())
else:
    """Bokehサーバー実行用"""
    viewer = AllInOneViewer()
    document = curdoc()
    document.add_root(viewer.get_view())
