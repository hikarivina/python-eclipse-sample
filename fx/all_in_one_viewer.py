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
from bokeh.models.widgets import Select, TextInput
from bokeh.io import curdoc

output_file("all-in-one_viewer.html")


class AllInOneViewer(object):
    """ AllInOneViewer - All-in-One FX Viewer定義クラス。"""

    def __init__(self):
        """"コンストラクタ
        Args:
            None
        """
        self.debug_text_ins = TextInput(value="default", title="debug text:")
        self.debug_text_gra = TextInput(value="default", title="debug text:")

        # Widgetセレクト（通貨ペア）
        self.__widsel_ins = Select(title="通貨ペア:",
                                   value="USD-JPY",
                                   options=["USD-JPY", "EUR-JPY", "EUR-USD"])
        self.__widsel_ins.on_change("value", self.__sel_ins_callback)

        # Widgetセレクト（期間）
        self.__widsel_gra = Select(title="期間:",
                                   value="日足",
                                   options=["週足", "日足", "４時間足", "１時間足",
                                            "３０分足", "１５分足", "１０分足",
                                            "５分足", "１分足"])
        self.__widsel_gra.on_change("value", self.__sel_gra_callback)

        self.__view = gridplot([[self.__widsel_ins, self.__widsel_gra],
                                [self.debug_text_ins, self.debug_text_gra],
                                [None, None],
                                [None, None]])

    def get_view(self):
        return self.__view

    def __sel_ins_callback(self, attr, old, new):
        """Widgetセレクト（通貨ペア）コールバックメソッド
        Args:
            attr (str) : An attribute name on this object
            old (str) : Old value
            new (str) : New value
        Returns:
            None
        """
        self.debug_text_ins.value = new

    def __sel_gra_callback(self, attr, old, new):
        """Widgetセレクト（期間）コールバックメソッド
        Args:
            attr (str) : An attribute name on this object
            old (str) : Old value
            new (str) : New value
        Returns:
            None
        """
        self.debug_text_gra.value = new


if __name__ == "__main__":
    """eclipse実行用"""
    viewer = AllInOneViewer()
    show(viewer.get_view())
else:
    """Bokehサーバー実行用"""
    viewer = AllInOneViewer()
    document = curdoc()
    document.add_root(viewer.get_view())
