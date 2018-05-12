from enums import PieceColor


class Controller:
    def __init__(self, game):
        self.move_complete = []
        self.__game = game
        self.__current_move_color = PieceColor.WHITE

    def make_move(self, move):
        piece = self.__game.get_current_state().get(move.start_cell)
        if piece is None or piece.color != self.__current_move_color:
            return

        if self.__game.try_make_move(move):
            self.__current_move_color = PieceColor.invert(self.__current_move_color)
            self.__game.current_move_color = self.__current_move_color
            for func in self.move_complete:
                func(PieceColor.invert(self.__current_move_color))

