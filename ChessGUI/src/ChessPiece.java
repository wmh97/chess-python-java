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

    public void refreshPiece(){

        this.setBounds(
                (int)this.getPosition().getX(),
                (int)this.getPosition().getY(),
                this.boardWidth/8,
                this.boardHeight/8
        );

    }

    public Point getDropSquare(Point droppedPos){

        // get the position, work out which square it is in,
        // then drop it to the centre of that square.
        double xPos = droppedPos.getX();
        double yPos = droppedPos.getY();

        System.out.println("drop square number");
        System.out.println(
                BoardSquare.calcSquareNumber((int)xPos, (int)yPos)
        );

        int squareNumber = BoardSquare.calcSquareNumber((int)xPos, (int)yPos);
        int squareCentredXPos = BoardSquare.calcBoardXPos(squareNumber, boardWidth);
        int squareCentredYPos = BoardSquare.calcBoardYPos(squareNumber, boardHeight);

        // These coords are actually the corner of the square, but the
        // label position is set by the corner of the label, so setting the corner
        // of the label to the corner of the square means the piece is centred.
        Point centredPos = new Point(squareCentredXPos, squareCentredYPos);
        return centredPos;

    }

}
