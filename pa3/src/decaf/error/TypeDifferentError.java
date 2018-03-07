package decaf.error;

import decaf.Location;

/**
 * example：function 'gotoMars' expects 1 argument(s) but 3 given<br>
 * PA2
 */
public class TypeDifferentError extends DecafError {

	private String type;
	private String type2;

	public TypeDifferentError(Location location, String type, String type2) {
		super(location);
		this.type = type;
		this.type2 = type2;
	}

	@Override
	protected String getErrMsg() {
		return "type: " + type + " is different with other expr's type " + type2;
	}
}
