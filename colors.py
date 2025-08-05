class Colors:
   
    dark_grey=(26,31,40)
    green = (47,230,23)
    red = (255,0,0)
    blue = (0,0,255)
    orange = (226,116,17)
    yellow = (237,234,4)
    cyan = (21,204,209)
    purple = (166,0,247)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.blue, cls.orange, cls.yellow, cls.cyan, cls.purple]