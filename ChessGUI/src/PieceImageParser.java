import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class PieceImageParser {

    private Image[] pieceSubImages;

    PieceImageParser(String imagePath){

        Image[] pieceSubImages = new Image[12];

        try {
            BufferedImage pieceImages = ImageIO.read(new File(imagePath));

            int pieceWidth = (pieceImages.getWidth()/6);
            int pieceHeight = (pieceImages.getHeight()/2);
            int imgIndex = 0;

            for (int imgXPos=0; imgXPos<=pieceImages.getWidth()-pieceWidth; imgXPos+=pieceWidth){
                for (int imgYPos=0; imgYPos<=pieceImages.getHeight()-pieceHeight; imgYPos+=pieceHeight){

                    //System.out.println(String.format("imgXPos=%d, imgYPos=%d, imgIndex=%d", imgXPos, imgYPos, imgIndex));

//                    ImageIO.write(
//                            pieceImages.getSubimage(imgXPos, imgYPos, pieceWidth, pieceHeight),
//                            "png",
//                            new File(String.format("src//%d.png", imgIndex))
//                    );

                    pieceSubImages[imgIndex] = pieceImages.getSubimage(imgXPos, imgYPos, pieceWidth, pieceHeight);
                    imgIndex++;

                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        setSubImages(pieceSubImages);

    }

    public Image[] getSubImages(){
        return this.pieceSubImages;
    }

    public void setSubImages(Image[] pieceSubImages){
        this.pieceSubImages = pieceSubImages;
    }

    public Image getWhiteKing(){
        return getSubImages()[0];
    }
    public Image getBlackKing(){
        return getSubImages()[1];
    }
    public Image getWhiteQueen(){
        return getSubImages()[2];
    }
    public Image getBlackQueen(){
        return getSubImages()[3];
    }
    public Image getWhiteBishop(){
        return getSubImages()[4];
    }
    public Image getBlackBishop(){
        return getSubImages()[5];
    }
    public Image getWhiteKnight(){
        return getSubImages()[6];
    }
    public Image getBlackKnight(){
        return getSubImages()[7];
    }
    public Image getWhiteRook(){
        return getSubImages()[8];
    }
    public Image getBlackRook(){
        return getSubImages()[9];
    }
    public Image getWhitePawn(){
        return getSubImages()[10];
    }
    public Image getBlackPawn(){
        return getSubImages()[11];
    }

}
