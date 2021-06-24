import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ChessPiece extends JLabel{

    private Point position;
    private ImageIcon pieceIcon;

    JLabel pieceLabel;

    private int boardWidth;
    private int boardHeight;

    ChessPiece(char pieceSymbol, int squareNumber, int boardWidth, int boardHeight){

        this.boardWidth = boardWidth;
        this.boardHeight = boardHeight;

        // piece is a label with a png icon on it.
        // setting the image based on the piece symbol.
        switch(pieceSymbol){
            case 'p': setIcon("src\\piece.png", boardWidth/16, boardHeight/10);
            break;
            default: return;
        }
        setPosition(squareNumber, boardWidth);

    }

    public ImageIcon getIcon(){
        return this.pieceIcon;
    }

    public void setIcon(String iconPath, int width, int height){
        ImageIcon icon = new ImageIcon(iconPath);
        this.pieceIcon = resizeIcon(icon, width, height);
    }

    private ImageIcon resizeIcon(ImageIcon icon, int width, int height){

        Image image = icon.getImage(); // transform it
        Image newImage = image.getScaledInstance(width, height, java.awt.Image.SCALE_SMOOTH); // scale it the smooth way

        return (new ImageIcon(newImage)); // transform it back
    }

    public Point getPosition(){
        return this.position;
    }

    public void setPosition(int squareNumber, int boardLength){
        this.position = new Point( BoardSquare.calcBoardXPos(squareNumber, boardLength),
                                   BoardSquare.calcBoardYPos(squareNumber, boardLength) );
    }

    public void setPosition(Point pos){
        this.position = new Point((int)pos.getX(), (int)pos.getY());
    }

    public JLabel addLabel(){

        this.setIcon(this.getIcon());
        this.setVerticalAlignment(JLabel.CENTER);
        this.setHorizontalAlignment(JLabel.CENTER);
        this.setBounds(
                (int)this.getPosition().getX(),
                (int)this.getPosition().getY(),
                this.boardWidth/8,
                this.boardHeight/8
        );
        this.setVisible(true);

        return this;
    }

}
