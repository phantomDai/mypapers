// This is a mutant program.
// Author : ysma

import java.util.Scanner;


public class ExpenseReimbursementSystem
{

    private java.lang.String levelOfSalesStaff;

    private double allowableMileage;

    private double costPerKilometer;

    public  double calculateReimbursementAmount( java.lang.String stafflevel, double actualmonthlymileage, double monthlysalesamount, double airfareamount, double otherexpensesamount )
    {
        double feeForOverUseOfCar;
        double airfareReimbursement;
        double reimbursementsOtherThanAirfare;
        feeForOverUseOfCar = costPerKilometer * (actualmonthlymileage - allowableMileage);
        if (stafflevel.equals( "seniormanager" )) {
            airfareReimbursement = airfareamount;
        } else {
            if (stafflevel.equals( "manager" )) {
                if (monthlysalesamount >= 50000) {
                    airfareReimbursement = airfareamount;
                } else {
                    airfareReimbursement = 0;
                }
            } else {
                if (stafflevel.equals( "supervisor" )) {
                    if (monthlysalesamount >= 80000) {
                        airfareReimbursement = airfareamount;
                    } else {
                        airfareReimbursement = 0;
                    }
                } else {
                    new java.io.IOException( "Invalid stafflevel" );
                    airfareReimbursement = 0;
                }
            }
        }
        if (monthlysalesamount >= 100000) {
            reimbursementsOtherThanAirfare = otherexpensesamount;
        } else {
            reimbursementsOtherThanAirfare = 0;
        }
        double totalReimbursementAmount = -feeForOverUseOfCar + airfareReimbursement + reimbursementsOtherThanAirfare;
        return totalReimbursementAmount;
    }

    public static  void main( java.lang.String[] args )
    {
        java.util.Scanner s = new java.util.Scanner( System.in );
        java.lang.String stafflevel = null;
        System.out.println( "please enter stafflevel:" );
        stafflevel = s.next();
        System.out.println( "please enter actual monthly mileage:" );
        double actualmonthlymileage = s.nextDouble();
        System.out.println( "please enter monthly sales amount:" );
        double monthlysalesamount = s.nextDouble();
        System.out.println( "please enter airfare:" );
        double airfare = s.nextDouble();
        System.out.println( "please enter other expenses:" );
        double otherexpenses = s.nextDouble();
        ExpenseReimbursementSystem sys = new ExpenseReimbursementSystem();
        double amount = sys.calculateReimbursementAmount( stafflevel, actualmonthlymileage, monthlysalesamount, airfare, otherexpenses );
        System.out.println( "total reimbursement amount: " + String.valueOf( amount ) );
    }

}
