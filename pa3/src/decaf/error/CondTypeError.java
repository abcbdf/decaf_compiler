package decaf.error;

import decaf.Location;

public class CondTypeError extends DecafError {

	private String name;

	public CondTypeError(Location location, String name) {
		super(location);
		this.name = name;
	}

	@Override
	protected String getErrMsg() {
		return "The condition of Do Stmt requestd type bool but " + name + " given";
	}

}
