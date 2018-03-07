package decaf.error;

import decaf.Location;


public class MemberVarError extends DecafError {

	public MemberVarError(Location location) {
		super(location);
	}

	@Override
	public String getErrMsg() {
		return "super.member_var is not supported";
	}

}
