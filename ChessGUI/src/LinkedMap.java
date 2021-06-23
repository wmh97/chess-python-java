public class LinkedMap {

    private char[] squareSymbols;

    LinkedMap(){

        char[] squareSymbols = new char[64];
        char tempSymbol;
        char symbol1 = '-';
        char symbol2 = '+';
        int fileNumber = 1;

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

        }

        this.setSquareSymbols(squareSymbols);

    }

    public char[] getSquareSymbols(){
        return this.squareSymbols;
    }

    public void setSquareSymbols(char [] squareSymbols){
        this.squareSymbols = squareSymbols;
    }

}
