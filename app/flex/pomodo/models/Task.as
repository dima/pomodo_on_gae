package pomodo.models {
  import org.ruboss.models.RubossModel;
  
  [Resource(name="tasks")]
  [Bindable]
  public class Task extends RubossModel {
    public static const LABEL:String = "name";

    public var name:String;

    public var notes:String;

    [DateTime]
    public var startTime:Date;

    [DateTime]
    public var endTime:Date;

    public var completed:Boolean;

    public var nextAction:Boolean;

    [BelongsTo]
    public var project:Project;

    [BelongsTo]
    public var location:Location;

    [BelongsTo]
    public var user:User;

    public function Task() {
      super(LABEL);
    }
  }
}
