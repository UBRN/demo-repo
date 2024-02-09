// In Java, a class is a blueprint from which individual objects are created. 
// The class defines fields (attributes) and methods (behaviors) that the created objects can have.

public class bicycle {
    // Fields (attributes)
    private int gear;
    private int speed;

    //Constructor
    public bicycle(int gear,int speed) {
        this.gear = gear;
        this.speed = speed;
    }

    // Methods (behaviors)
    public void applyBrake (int decrement) {
        speed -= decrement;
    }
    public void speedUp (int increment) {
        speed += increment;
    }
    public String toString () {
        return ("no gears are " + gear + "\n" + "speed of bicycle is " + speed);
    }
}