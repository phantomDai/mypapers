import java.io.IOException;

public class BillCalculation
{

    private java.lang.String planType = "";

    private int planFee = 0;   //�ƻ�����

    private int talkTime = 0;   //�Ի�ʱ��

    private int flow = 0;       //����������

    private int callViewTime = 0;   //��Ƶͨ��ʱ�䣿

    private double talkTimePer = 0;  //ÿ���ӷ��ã�															

    private double flowPer = 0.3;    //����ÿ�׷��ã�

    private double viewPer = 0.6;

    private int talkTimeBench = 0;  //�ײ���ͨ��ʱ����

    private int flowBench = 0;    //�ײ�������

    private double bill = 0;

    public double phoneBillCalculation( java.lang.String planType, int planFee, int talkTime, int flow )
    {
        if (planType == "A" || planType == "a") {
            switch (planFee) {
            case 46 :
                talkTimeBench = 50;
                flowBench = 150;
                talkTimePer = 0.25;
                break;

            case 96 :
                talkTimeBench = 96;
                flowBench = 240;
                talkTimePer = 0.15;
                break;

            case 286 :
                talkTimeBench = 286;
                flowBench = 900;
                talkTimePer = 0.15;
                break;

            case 886 :
                talkTimeBench = 3000;
                flowBench = 3000;
                talkTimePer = 0.15;
                break;
			case 990:
				break;

            default  :
                new java.io.IOException( "Invalid planFee!" );

            }
        } else {
            if (planType == "B" || planType == "b") {
                switch (planFee) {
                case 46 :
                    talkTimeBench = 120;
                    flowBench = 40;
                    talkTimePer = 0.25;
                    break;

                case 96 :
                    talkTimeBench = 450;
                    flowBench = 80;
                    talkTimePer = 0.15;
                    break;

                case 126 :
                    talkTimeBench = 680;
                    flowBench = 100;
                    talkTimePer = 0.15;
                    break;

                case 186 :
                    talkTimeBench = 1180;
                    flowBench = 150;
                    talkTimePer = 0.15;
                    break;

                default  :
                    new java.io.IOException( "Invalid planFee" );

                }
            } else {
                new java.io.IOException( "Invalid planType!" );
            }
        }
        if (talkTime < talkTimeBench) {
            talkTime = talkTimeBench;
        }
        if (flow < flowBench) {
            flow = flowBench;
        }
        bill = (talkTime - talkTimeBench) * talkTimePer + (flow - flowBench) * flowPer + planFee;
        //bill = (talkTimeBench) * talkTimePer + (flow - flowBench) * flowPer + planFee;
        return bill;
    }
}
