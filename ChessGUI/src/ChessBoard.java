import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ChessBoard extends JLayeredPane{

    private int boardWidth;
    private int boardHeight;

    JLabel piece;
    JLabel marker;

    ChessBoard(int width, int height){


        this.setBoardWidth(width);
        this.setBoardHeight(height);
        this.setBounds(0, 0, getBoardWidth(), getBoardHeight());

        // prototype linked map data structure mimicking what linked map will be.
        // getting the square colour data as an array of chars.
        GameData gameData = new GameData();

        this.addSquares(gameData.getSquareSymbols());
        this.addPieces(gameData.getPieceSymbols());
        this.addPieceListeners();
        //this.addSquareListeners();

    }

    public int getBoardWidth(){
        return this.boardWidth;
    }
    public void setBoardWidth(int width){
        this.boardWidth = width;
    }
    public int getBoardHeight(){
        return this.boardHeight;
    }
    public void setBoardHeight(int height){
        this.boardHeight = height;
    }

    private void addSquares(char[] squareSymbols){
        for (int i=1; i<=squareSymbols.length; i++){

            int squareIndex = (i-1);
            this.add(
                    new BoardSquare(squareSymbols[squareIndex], squareIndex, this.getBoardWidth(), this.getBoardHeight()),
                    Integer.valueOf(0)
            );

        }
    }

    private void addPieces(char[] pieceSymbols){
        for (int i=1; i<=pieceSymbols.length; i++){
            if (pieceSymbols[i-1] != ' '){

                int squareIndex = i-1;

                ChessPiece piece = new ChessPiece(
                        pieceSymbols[squareIndex], squareIndex, getBoardWidth(), getBoardHeight()
                );

                this.add(piece.addLabel(), Integer.valueOf(1));

            }
        }
    }

    private void setPaneLayer(Component component, int layer){
        this.setLayer(component, Integer.valueOf(Integer.toString(layer)));
    }

    private void addPieceListeners(){

        for (Component component : this.getComponents()){
            if (component instanceof JLabel){

                piece = (JLabel) component;
                ChessPiece selectedPiece = (ChessPiece) component;

                selectedPiece.addMouseListener(
                        new MouseListener() {
                            @Override
                            public void mouseClicked(MouseEvent e) {}

                            @Override
                            public void mousePressed(MouseEvent e) {}

                            @Override
                            public void mouseReleased(MouseEvent e) {
                                movePiece(selectedPiece, e, true);
                            }

                            @Override
                            public void mouseEntered(MouseEvent e) {}
                            @Override
                            public void mouseExited(MouseEvent e) {}
                        }
                );

                selectedPiece.addMouseMotionListener(
                        new MouseMotionAdapter() {
                            // whenever the mouse is moved...
                            @Override
                            public void mouseDragged(MouseEvent e) {
                                movePiece(selectedPiece, e, false);
                            }
                        }
                );
            }
        }
    }

//    private void addSquareListeners(){
//        for (Component component : this.getComponents()) {
//            if (component instanceof JPanel) {;
//
//                JPanel currentSquare = (JPanel) component;
//
//                currentSquare.addMouseListener(
//                        new MouseListener() {
//
//                            boolean highlight;
//                            JLabel marker;
//
//                            @Override
//                            public void mouseClicked(MouseEvent e) {
//
//                            }
//
//                            @Override
//                            public void mousePressed(MouseEvent e) {
//                                highlight = true;
//                            }
//
//                            @Override
//                            public void mouseReleased(MouseEvent e) {
//                                highlight = false;
//                            }
//
//                            @Override
//                            public void mouseEntered(MouseEvent e) {
//
//                                System.out.println("entered panel....");
//                                marker = new JLabel();
//                                marker.setText("X");
//                                marker.setVerticalAlignment(JLabel.CENTER);
//                                marker.setHorizontalAlignment(JLabel.CENTER);
//                                marker.setFont(new Font("Ariel", Font.BOLD, 50));
//                                marker.setForeground(new Color(0xFFFF00)); // yellow
//                                marker.setBounds(0, 0, boardWidth / 8, boardHeight / 8);
//
//                                currentSquare.add(marker);
//                                currentSquare.revalidate();
//                                currentSquare.repaint();
//
//                            }
//
//                            @Override
//                            public void mouseExited(MouseEvent e) {
//                                    currentSquare.remove(marker);
//                                    currentSquare.revalidate();
//                                    currentSquare.repaint();
//
//                            }
//                        }
//                );
//            }
//        }
//    }

    private void movePiece(ChessPiece piece, MouseEvent e, boolean dropped){

        // the listener is on the label itself so the coordinate is relative
        // to the corner of the label (0,0). Therefore any movement will simply
        // cause an offset from zero on this coordinate.
        Point newPos = e.getPoint();

        System.out.println(newPos);

        // making a point at the centre of the piece label.
        // This coordinate is relative to the whole board.
        Point piecePos = new Point(
                (int)piece.getPosition().getX() - (int)getBoardWidth()/16,
                (int)piece.getPosition().getY() - (int)getBoardHeight()/16
        );

        // moving the piece label by the amount the mouse has moved.
        // i.e. the offset from zero.
        piecePos.translate((int)newPos.getX(), (int)newPos.getY());

        piece.setPosition(piecePos);

        // leaves behind label on square after move - this might be a good thing though.
        highlightPositionSquare(piecePos); /////////////////////////////////////////

        if (!dropped){
            setPaneLayer(piece, 2); // layer 2 means the piece will appear above others while being dragged.
            piece.setPosition(piecePos);
        } else {
            setPaneLayer(piece, 1);
            Point dropSquare = piece.getDropSquare(piecePos);
            piece.setPosition(dropSquare);
        }

        piece.refreshPiece();
    }

    private void highlightPositionSquare(Point position){

        for (Component component : this.getComponents()){

            // if component has the same position as the position passed in...
            if (component instanceof JPanel){

                int componentSquareNumber = BoardSquare.calcSquareNumber(component.getX(), component.getY());
                int positionSquareNumber = BoardSquare.calcSquareNumber((int)position.getX(), (int)position.getY());

                //System.out.println(String.format("panelNo. = %d, currposNo. = %d", componentSquareNumber, positionSquareNumber ));

                if (componentSquareNumber == positionSquareNumber){

                    // getting the pos marker associated with a square and
                    // adding it to the square.
                    BoardSquare square = (BoardSquare) component;
                    JLabel marker = square.getSquarePosMarker();
                    square.add(marker);

                    square.revalidate();
                    square.repaint();

                } else {

                    // ******** inefficient???? ************
                    // ******** also might be slow for the first piece move **********
                    BoardSquare square = (BoardSquare) component;
                    square.removeSquarePosMarker();

                }
            }

        }
    }

    private void removeHighlightFromSquare(JPanel square){
        for (Component component: square.getComponents()){
            if (component instanceof JLabel){
                square.remove(component);
            }
        }
    }

}
