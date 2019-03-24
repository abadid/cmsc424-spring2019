package com.match.model;

public enum Organ {

	Heart, Liver, Kidney, Lung, Pancreas;

	public String toString(){
		switch(this){
			case Heart:
				return "Heart";
			case Liver:
				return "Liver";
			case Kidney:
				return "Kidney";
			case Lung:
				return "Lung";
			case Pancreas:
				return "Pancreas";
		}
		return null;
	}

	public static Organ fromString(String s){
		switch(s){
			case "Heart":
				return Organ.Heart;
			case "Liver":
				return Organ.Liver;
			case "Kidney":
				return Organ.Kidney;
			case "Lung":
				return Organ.Lung;
			case "Pancreas":
				return Organ.Pancreas;
		}
		return null;
	}
}
