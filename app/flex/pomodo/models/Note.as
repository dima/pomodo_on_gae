package pomodo.models {
  import org.ruboss.models.RubossModel;
  
  [Resource(name="notes")]
  [Bindable]
  public class Note extends RubossModel {
    public static const LABEL:String = "content";

    public var content:String = "";

    [BelongsTo]
    public var account:Account;

    public function Note() {
      super(LABEL);
    }
  }
}
