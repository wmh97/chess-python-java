import java.awt.*;
import java.awt.event.*;
import java.util.HashMap;
import javax.swing.*;

public class ChessPiece extends JLabel{

    static HashMap<Integer, ChessPiece> squareNumberPieceMap = new HashMap<Integer, ChessPiece>();
    private static int squareNumber = 0;

    private Point position;
    private ImageIcon pieceIcon;

    JLabel pieceLabel;

    private int boardWidth;
    private int boardHeight;

    static PieceImageParser pieceImageParser;
    static ImageIcon whiteKing;
    static ImageIcon whiteQueen;
    static ImageIcon whiteBishop;
    static ImageIcon whiteKnight;
    static ImageIcon whiteRook;
    static ImageIcon whitePawn;
    static ImageIcon blackKing;
    static ImageIcon blackQueen;
    static ImageIcon blackBishop;
    static ImageIcon blackKnight;
    static ImageIcon blackRook;
    static ImageIcon blackPawn;

    ChessPiece(String pieceSymbol, int squareNumber, int boardWidth, int boardHeight){

        this.boardWidth = boardWidth;
        this.boardHeight = boardHeight;

        // piece is a label with a png icon on it.
        // setting the image based on the piece symbol.
        switch(pieceSymbol){
            case "br":  setPieceIcon(blackRook, boardWidth/8, boardHeight/8);
            break;
            case "bk": setPieceIcon(blackKnight, boardWidth/8, boardHeight/8);
            break;
            case "bb": setPieceIcon(blackBishop, boardWidth/8, boardHeight/8);
            break;
            case "bQ": setPieceIcon(blackQueen, boardWidth/8, boardHeight/8);
            break;
            case "bK": setPieceIcon(blackKing, boardWidth/8, boardHeight/8);
            break;
            case "bp": setPieceIcon(blackPawn, boardWidth/8, boardHeight/8);
            break;
            case "wr": setPieceIcon(whiteRook, boardWidth/8, boardHeight/8);
            break;
            case "wk": setPieceIcon(whiteKnight, boardWidth/8, boardHeight/8);
            break;
            case "wb": setPieceIcon(whiteBishop, boardWidth/8, boardHeight/8);
            break;
            case "wQ": setPieceIcon(whiteQueen, boardWidth/8, boardHeight/8);
            break;
            case "wK": setPieceIcon(whiteKing, boardWidth/8, boardHeight/8);
            break;
            case "wp": setPieceIcon(whitePawn, boardWidth/8, boardHeight/8);
            break;
            default: return; // throw error
        }
        setPosition(squareNumber, boardWidth);

        ChessPiece.squareNumberPieceMap.put(squareNumber, this);
        squareNumber++;

    }

    public ImageIcon getPieceIcon(){
        return this.pieceIcon;
    }

    public void setPieceIcon(String iconPath, int width, int height){
        ImageIcon icon = new ImageIcon(iconPath);
        this.pieceIcon = resizeIcon(icon, width, height);
    }

    public void setPieceIcon(ImageIcon icon, int width, int height){
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

        // remove the old position from the hash map and add the new one,
        // only if we have a position stored already.
        if (this.position != null){
            ChessPiece.squareNumberPieceMap.remove(
                    BoardSquare.calcSquareNumber((int)this.position.getX(), (int)this.position.getY())
            );
            ChessPiece.squareNumberPieceMap.put(squareNumber, this);
        }

        int newXPos = BoardSquare.calcBoardXPos(squareNumber, boardLength);
        int newYPos = BoardSquare.calcBoardYPos(squareNumber, boardLength);
        this.position = new Point(newXPos, newYPos);
    }

    public void setPosition(Point pos){
        this.position = new Point((int)pos.getX(), (int)pos.getY());
    }

    public JLabel addLabel(){

        this.setIcon(this.getPieceIcon());
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

    public void movePiece(MouseEvent e, boolean dropped){

        // the listener is on the label itself so the coordinate is relative
        // to the corner of the label (0,0). Therefore any movement will simply
        // cause an offset from zero on this coordinate.
        Point newPos = e.getPoint();

        System.out.println(newPos);

        // making a point at the centre of the piece label.
        // This coordinate is relative to the whole board.
        Point piecePos = new Point(
                (int)this.getPosition().getX() - (int)boardWidth/16,
                (int)this.getPosition().getY() - (int)boardHeight/16
        );

        // moving the piece label by the amount the mouse has moved.
        // i.e. the offset from zero.
        piecePos.translate((int)newPos.getX(), (int)newPos.getY());

        this.setPosition(piecePos);

        // leaves behind label on square after move - this might be a good thing though.
        // *************************************************************************************************************
         // **** NOTE: this is making the first move slow for some reason ************
        // ***** must be because none of the squares are highlighted with label????? ***********************************
        ChessBoard.highlightPositionSquare(piecePos);

        if (!dropped){
            this.setPosition(piecePos);
        } else {
            Point dropSquare = this.getDropSquare(piecePos);
            this.setPosition(dropSquare);
        }
        this.refreshPiece();
    }

    public Point getDropSquare(Point droppedPos){

        // get the position, work out which square it is in,
        // then drop it to the centre of that square.
        double xPos = droppedPos.getX();
        double yPos = droppedPos.getY();

        System.out.println(String.format("Drop Square No. %d", BoardSquare.calcSquareNumber((int)xPos, (int)yPos)));

        int squareNumber = BoardSquare.calcSquareNumber((int)xPos, (int)yPos);
        int squareCentredXPos = BoardSquare.calcBoardXPos(squareNumber, boardWidth);
        int squareCentredYPos = BoardSquare.calcBoardYPos(squareNumber, boardHeight);

        // These coords are actually the corner of the square, but the
        // label position is set by the corner of the label, so setting the corner
        // of the label to the corner of the square means the piece is centred.
        Point centredPos = new Point(squareCentredXPos, squareCentredYPos);
        return centredPos;

    }

    static void parsePieceImages(String allPiecesImage){

        PieceImageParser parsePieceImages = new PieceImageParser(allPiecesImage);

        whiteKing = new ImageIcon(parsePieceImages.getWhiteKing());

        System.out.println(whiteKing);

        whiteQueen = new ImageIcon(parsePieceImages.getWhiteQueen());
        whiteBishop = new ImageIcon(parsePieceImages.getWhiteBishop());
        whiteKnight = new ImageIcon(parsePieceImages.getWhiteKnight());
        whiteRook = new ImageIcon(parsePieceImages.getWhiteRook());
        whitePawn = new ImageIcon(parsePieceImages.getWhitePawn());

        blackKing = new ImageIcon(parsePieceImages.getBlackKing());
        blackQueen = new ImageIcon(parsePieceImages.getBlackQueen());
        blackBishop = new ImageIcon(parsePieceImages.getBlackBishop());
        blackKnight = new ImageIcon(parsePieceImages.getBlackKnight());
        blackRook = new ImageIcon(parsePieceImages.getBlackRook());
        blackPawn = new ImageIcon(parsePieceImages.getBlackPawn());

    }

}
