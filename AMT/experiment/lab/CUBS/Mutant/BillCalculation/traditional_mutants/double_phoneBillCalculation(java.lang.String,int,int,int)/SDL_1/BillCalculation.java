// This is a mutant program.
// Author : ysma

import java.io.IOException;


public class BillCalculation
{

    private java.lang.String planType = "";

    private int planFee = 0;

    private int talkTime = 0;

    private int flow = 0;

    private int callViewTime = 0;

    private double talkTimePer = 0;

    private double flowPer = 0.3;

    private double viewPer = 0.6;

    private int talkTimeBench = 0;

    private int flowBench = 0;

    private double bill = 0;

    public  double phoneBillCalculation( java.lang.String planType, int planFee, int talkTime, int flow )
    {
        if (talkTime < talkTimeBench) {
            talkTime = talkTimeBench;
        }
        if (flow < flowBench) {
            flow = flowBench;
        }
        bill = (talkTime - talkTimeBench) * talkTimePer + (flow - flowBench) * flowPer + planFee;
        return bill;
    }

}
