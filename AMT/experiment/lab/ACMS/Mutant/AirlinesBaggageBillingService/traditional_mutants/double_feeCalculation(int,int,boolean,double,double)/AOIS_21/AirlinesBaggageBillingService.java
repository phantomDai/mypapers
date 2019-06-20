// This is a mutant program.
// Author : ysma

public class AirlinesBaggageBillingService
{

    double benchmark = 0;

    double luggagefee = 0;

    public  double feeCalculation( int airClass, int area, boolean isStudent, double luggage, double economicfee )
    {
        switch (airClass) {
        case 0 :
            benchmark = 40.0;
            break;

        case 1 :
            benchmark = 30.0;
            break;

        case 2 :
            benchmark = 20.0;
            break;

        case 3 :
            benchmark = 0.0;
            break;

        }
        if (area == 1) {
            if (isStudent) {
                benchmark = 30.0;
            }
        }
        if (benchmark > luggage) {
            luggage = benchmark;
        }
        return luggagefee = (luggage++ - benchmark) * economicfee * 0.015;
    }

}
