import javax.swing.*;
import java.awt.*;

public class Main {

    public static void main(String[] args){

        JFrame userInterface;
        ChessBoard chessBoard;

        userInterface = new JFrame("Chess");

        userInterface.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        userInterface.setSize(750, 750);
        userInterface.setResizable(true);
        userInterface.setLayout(null);

        chessBoard = new ChessBoard(720, 720);

        userInterface.add(chessBoard);
        userInterface.setVisible(true);
    }
}
