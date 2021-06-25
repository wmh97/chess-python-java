import javax.swing.*;

public class UserInterface extends JFrame {

    ChessBoard chessBoard;

    UserInterface(int width, int height){

        int frameWidth = (int) (width * 1.1);
        int frameHeight = (int) (height * 1.1);

        this.setTitle("Chess");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setSize(frameWidth, frameHeight);
        this.setResizable(true);
        this.setLayout(null);

        chessBoard = new ChessBoard(width, height);

        this.add(chessBoard);
        this.setVisible(true);

    }

}
