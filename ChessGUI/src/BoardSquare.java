import javax.swing.*;
import java.awt.*;

public class BoardSquare extends JPanel{

    JLabel testPiece;
    ImageIcon testPieceIcon;

    BoardSquare(char squareSymbol){

        // setting the square colour to white or black depending on the
        // square symbol.
        if (squareSymbol == '+'){
            this.setBackground(Color.white);
        } else if (squareSymbol == '-'){
            this.setBackground(Color.black);
        }

        // adding a piece to the square.
        // piece is a label with a png icon on it.
        testPiece = new JLabel();
        testPieceIcon = resizeIcon(new ImageIcon("src\\piece.png"), 50, 75);

        testPiece.setIcon(testPieceIcon);
        testPiece.setVerticalAlignment(JLabel.CENTER);
        testPiece.setHorizontalAlignment(JLabel.CENTER);

        this.add(testPiece);

    }

    private ImageIcon resizeIcon(ImageIcon icon, int width, int height){

        Image image = icon.getImage(); // transform it
        Image newImage = image.getScaledInstance(width, height,  java.awt.Image.SCALE_SMOOTH); // scale it the smooth way

        return (new ImageIcon(newImage)); // transform it back
    }

}
