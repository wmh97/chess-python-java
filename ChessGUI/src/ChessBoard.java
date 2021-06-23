import javax.swing.*;
import java.awt.*;

public class ChessBoard extends JFrame{

    ChessBoard(int width, int height){

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(width, height);
        this.setResizable(false);
        this.setLayout(new GridLayout(8,8,0,0));

    }

    static void addSquares(ChessBoard chessBoard, char[] squareSymbols){

        for (int i=1; i<=squareSymbols.length; i++){
            chessBoard.add( new BoardSquare(squareSymbols[i-1]) );
        }

    }
}
