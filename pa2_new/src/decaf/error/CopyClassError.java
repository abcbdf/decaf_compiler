package decaf.error;

import decaf.Location;

/**
 * example：class 'zig' not found<br>
 * PA2
 */
public class CopyClassError extends DecafError {

	private String name;

	public CopyClassError(Location location, String name) {
		super(location);
		this.name = name;
	}

	@Override
	protected String getErrMsg() {
		return "expected class type for copy expr but " + name + " given";
	}

}
