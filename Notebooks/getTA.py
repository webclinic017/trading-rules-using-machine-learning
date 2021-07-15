import pandas as pd 
import numpy as np 
from ta import momentum, trend, volatility, volume 
import ta

def get_ta(df_):
    """
    parameters
    df_ (pd.DataFrame): must contain [open,high,low,close,volume] in columns.
    window (list): list of windows, if None, use default windows
    """
    df = df_.copy()
    # assert error
    df.columns = [x.lower() for x in df.columns]
    

    df['m_rsi'] = momentum.rsi(df.close)
    df['m_roc'] = momentum.roc(df.close)
    df['m_wr']  = momentum.williams_r(df.high, df.low, df.close)
    df['vm_cmf'] = volume.chaikin_money_flow(df.high, df.low, df.close, df.volume)
    df['vm_mfi'] = volume.money_flow_index(df.high, df.low, df.close, df.volume)
    df['vm_fi'] = volume.force_index(df.close, df.volume)
    df['vm_eom'] = volume.ease_of_movement(df.high, df.low, df.volume)
    df['vl_bbp'] = volatility.bollinger_pband(df.close)
    df['vl_atr'] = volatility.average_true_range(df.high, df.low, df.close)
    df['t_macdd']  = trend.MACD(df.close).macd_diff()
    df['t_trix'] = trend.trix(df.close)
    df['t_cci'] = trend.cci(df.high, df.low, df.close)
    df['t_dpo'] = trend.dpo(df.close)  # trend occilator
    df['t_kst'] = trend.kst(df.close)  # know sure thing
    df['t_adx'] = trend.adx(df.high, df.low, df.close)  # adx:strength of trend
            
    return df 

def get_ta_window(df_, window):
    """
    parameters
    df_ (pd.DataFrame): must contain [open,high,low,close,volume] in columns.
    window (list): list of windows, if None, use default windows
    """
    df = df_.copy()
    # assert error
    df.columns = [x.lower() for x in df.columns]
    
    for w in window:
        df['m_rsi_{}'.format(w)] = momentum.rsi(df.close, window=w)
        df['m_roc_{}'.format(w)] = momentum.roc(df.close, window=w)
        df['m_wr_{}'.format(w)]  = momentum.williams_r(df.high, df.low, df.close, lbp=w)
        df['vm_cmf_{}'.format(w)] = volume.chaikin_money_flow(df.high, df.low, df.close, df.volume, window=w)
        df['vm_mfi_{}'.format(w)] = volume.money_flow_index(df.high, df.low, df.close, df.volume, window=w)
        df['vm_fi_{}'.format(w)] = volume.force_index(df.close, df.volume, window=w)
        df['vm_eom_{}'.format(w)] = volume.ease_of_movement(df.high, df.low, df.volume, window=w)
        df['vl_bbp_{}'.format(w)] = volatility.bollinger_pband(df.close, window=w)
        df['vl_atr_{}'.format(w)] = volatility.average_true_range(df.high, df.low, df.close, window=w)
        df['t_macdd_{},{}'.format(w*2,w)]  = trend.MACD(df.close, window_fast=w, window_slow=w*2).macd_diff()
        df['t_trix_{}'.format(w)] = trend.trix(df.close, window=w)
        df['t_cci_{}'.format(w)] = trend.cci(df.high, df.low, df.close, window=w)
        df['t_dpo_{}'.format(w)] = trend.dpo(df.close, window=w)  # trend occilator
        #df['t_kst_{}'.format(w)] = trend.kst(df.close)  # know sure thing
        df['t_adx_{}'.format(w)] = trend.adx(df.high, df.low, df.close, window=w)  # adx:strength of trend
            
    return df 


