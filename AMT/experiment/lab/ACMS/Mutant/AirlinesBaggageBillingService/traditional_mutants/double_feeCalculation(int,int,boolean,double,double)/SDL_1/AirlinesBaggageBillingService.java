// This is a mutant program.
// Author : ysma

public class AirlinesBaggageBillingService
{

    double benchmark = 0;

    double luggagefee = 0;

    public  double feeCalculation( int airClass, int area, boolean isStudent, double luggage, double economicfee )
    {
        if (area == 1) {
            if (isStudent) {
                benchmark = 30.0;
            }
        }
        if (benchmark > luggage) {
            luggage = benchmark;
        }
        return luggagefee = (luggage - benchmark) * economicfee * 0.015;
    }

}
