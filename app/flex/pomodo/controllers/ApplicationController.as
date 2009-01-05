package pomodo.controllers {
  import pomodo.models.*;
  import pomodo.commands.*;

	import mx.core.Application;		
  import org.ruboss.Ruboss;
  import org.ruboss.controllers.RubossApplicationController;
  import org.ruboss.utils.RubossUtils;

  public class ApplicationController extends RubossApplicationController {
    private static var controller:ApplicationController;
    
    public static var models:Array = [Location, Note, Project, Task]; /* Models */
    
    public static var commands:Array = []; /* Commands */
    
    public function ApplicationController(enforcer:SingletonEnforcer, extraServices:Array,
      defaultServiceId:int = -1) {
      super(commands, models, extraServices, defaultServiceId);
    }
    
    public static function get instance():ApplicationController {
      if (controller == null) initialize();
      return controller;
    }
    
    public static function initialize(extraServices:Array = null, defaultServiceId:int = -1,
      airDatabaseName:String = null):void {
      if (!RubossUtils.isEmpty(airDatabaseName)) Ruboss.airDatabaseName = airDatabaseName;
      controller = new ApplicationController(new SingletonEnforcer, extraServices,
        defaultServiceId);
    }
  }
}

class SingletonEnforcer {}
