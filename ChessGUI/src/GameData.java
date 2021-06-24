public class GameData {

    private char[] squareSymbols;
    private char[] pieceSymbols;

    GameData(){

        // temp way of generating the data structures that we need to set up the board.

        char[] squareSymbols = new char[64];
        char tempSymbol;
        char symbol1 = '-';
        char symbol2 = '+';
        int fileNumber = 1;

        char[] pieceSymbols = new char[64];

        for (int i=1; i<=64; i++){

            fileNumber++;

            if (i % 2 == 0 ){
                squareSymbols[i-1] = symbol1;
            } else {
                squareSymbols[i-1] = symbol2;
            }

            // swap the symbol characters every row. Won't need this when
            // we are reading symbols from the linked map.
            if (fileNumber > 8){
                tempSymbol = symbol2;
                symbol2 = symbol1;
                symbol1 = tempSymbol;
                fileNumber = 1;
            }

            if (i <= 16 || i > 48){
                pieceSymbols[i-1] = 'p';
            } else{
                pieceSymbols[i-1] = ' ';
            }

        }

        setSquareSymbols(squareSymbols);
        setPieceSymbols(pieceSymbols);

    }

    public char[] getSquareSymbols(){
        return this.squareSymbols;
    }

    public void setSquareSymbols(char [] squareSymbols){
        this.squareSymbols = squareSymbols;
    }

    public char[] getPieceSymbols(){
        return this.pieceSymbols;
    }

    public void setPieceSymbols(char [] pieceSymbols){
        this.pieceSymbols = pieceSymbols;
    }

}
