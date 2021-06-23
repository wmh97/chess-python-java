import javax.swing.*;
import java.awt.*;

public class Main {

    public static void main(String[] args){

        ChessBoard chessBoard = new ChessBoard(720, 720);

        // prototype linked map data structure mimicking what linked map will be.
        // getting the square colour data as an array of chars.
        LinkedMap linkedMap = new LinkedMap();
        char[] squareSymbols = linkedMap.getSquareSymbols();

        ChessBoard.addSquares(chessBoard, squareSymbols);
        chessBoard.setVisible(true);

    }
}
